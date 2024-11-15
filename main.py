import subprocess
import os
import time

from helpers.constants import DATA_DIR, RESULTS_DIR, MANY_DIR, script_paths


if __name__ == "__main__":
    TIMEOUT = 1  # seconds

    # List of input files. Get all files in directory
    input_files = sorted([os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR)
                          if os.path.isfile(os.path.join(DATA_DIR, f)) and f.endswith(
            '.txt')])
    assert input_files, "No input files found in data directory"

    # # Delete existing results file
    # if os.path.exists(RESULTS_DIR / "many.txt"):
    #     os.remove(RESULTS_DIR / "many.txt")

    runs = []
    # runs.append("none")
    # runs.append("few")
    # runs.append("alternate")
    runs.append("some")
    # runs.append("many")

    for run in runs:
        batch_start = time.time()
        output_file = RESULTS_DIR / f"{run}.txt"

        # Create file if it doesn't exist
        if not os.path.exists(output_file):
            with open(output_file, "w") as results:
                pass

        # Get existing solutions. Comment out for overwriting of results.
        result_exists = set()
        with open(RESULTS_DIR / f"{run}.txt", "r") as results:
            for line in results:
                result_exists.add(line.split()[0])

        for input_file_path in input_files:
            input_filename = input_file_path.split("/")[-1]
            if input_filename in result_exists:
                print(f"Skipping {input_filename}")
                continue
            print(f"Processing {input_filename}")

            run_start = time.time()
            try:
                process = subprocess.run(
                    ["python3", script_paths[run] / f"{run}.py"],
                    input=open(DATA_DIR / input_filename).read(),
                    text=True,
                    capture_output=True,
                    timeout=TIMEOUT
                )
                if process.returncode == 0:
                    result = process.stdout.strip()
                else:
                    result = process.stderr.splitlines()[
                        -1] if process.stderr else "Unknown error"
            except subprocess.TimeoutExpired:
                result = f"Timeout_{TIMEOUT}_s"

            print("\t"+result)
            print(f"\t{time.time() - run_start:.2f} seconds")

            # Append to results file
            with open(output_file, "a") as results:
                results.write(f"{input_filename} {result}\n")

        print(f"Batch completed in {time.time() - batch_start:.2f} seconds")
        print(f"Results saved to {RESULTS_DIR}")