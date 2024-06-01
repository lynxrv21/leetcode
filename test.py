import os
import subprocess
from pathlib import Path


def run_test_file(file_path: Path) -> tuple[int, str, str]:
    """Run a single test file and capture its output."""
    env = os.environ.copy()
    env["PYTHONPATH"] = str(file_path.parent.parent)
    result = subprocess.run(
        ["python", str(file_path)], capture_output=True, text=True, env=env
    )
    return result.returncode, result.stdout, result.stderr


def main():
    base_dir = Path(__file__).parent
    problem_files = list(base_dir.glob("**/*.py"))

    # Exclude __init__.py and utils.py or any non-problem scripts
    problem_files = [
        f
        for f in problem_files
        if f.name
        not in ("__init__.py", "utils.py", "test.py", "get_problem.py")
    ]

    all_tests_passed = True

    for problem_file in problem_files:
        returncode, stdout, stderr = run_test_file(problem_file)
        if returncode != 0:
            all_tests_passed = False
            print(f"Tests failed in {problem_file}:")
            print(stderr)
        else:
            print(f"Tests passed in {problem_file}")

    if all_tests_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")


if __name__ == "__main__":
    main()
