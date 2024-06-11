import argparse
from pathlib import Path
from random import choice

PROBLEMS_DIR = Path(".").parent


def check_complexity(file: Path, complexity: str) -> bool:
    with file.open("r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip().lower() == f"#{complexity}":
                return True
    return False


def get_problem_files(problems_dir: Path, complexity: str = None) -> [Path]:
    problem_files = []

    for subdir in problems_dir.iterdir():
        if subdir.is_dir():
            for file in subdir.glob("*.py"):
                if file.name not in ("__init__.py", "utils.py"):
                    if complexity is None or check_complexity(file, complexity):
                        problem_files.append(file)
    return problem_files


def create_problem_template(problem_file: Path, output_dir: Path) -> None:
    with problem_file.open("r") as file:
        lines = file.readlines()

    problem_statement = []
    test_cases = []
    problem_statement_flag = True
    test_cases_flag = False

    for line in lines:
        if line.startswith("def "):
            problem_statement_flag = False
            problem_statement.append(line)

        elif problem_statement_flag:
            problem_statement.append(line)
        elif line.strip() == 'if __name__ == "__main__":':
            test_cases_flag = True
            test_cases.append(line)
        elif test_cases_flag:
            test_cases.append(line)

    new_filename = output_dir / problem_file.name
    with new_filename.open("w") as new_file:
        new_file.writelines(problem_statement)
        new_file.writelines("    pass\n\n\n")
        new_file.writelines(test_cases)

    print(f"Generated problem file: {new_filename}")


def setup_parses():
    parser = argparse.ArgumentParser(
        description="Generate a problem template from existing LeetCode solutions."
    )
    parser.add_argument(
        "-c",
        "--complexity",
        type=str,
        choices=["easy", "medium", "hard"],
        help="Specify the complexity level of the problem (easy, medium, hard).",
    )
    parser.add_argument(
        "-p",
        "--problem",
        type=str,
        help="Specify the name of a specific problem file (without .py extension).",
    )
    return parser


def find_problem_file(problems_dir: Path, problem_name: str) -> Path | None:
    for subdir in problems_dir.iterdir():
        if subdir.is_dir():
            problem_file = subdir / f"{problem_name}.py"
            if problem_file.exists():
                return problem_file
    return None


def main() -> None:
    args = setup_parses().parse_args()
    complexity = args.complexity
    problem_name = args.problem

    base_dir = Path(__file__).parent

    if problem_name:
        problem_file = find_problem_file(base_dir, problem_name)
        if not problem_file:
            print(f"Problem file '{problem_name}.py' not found in any subdirectory.")
            return
        create_problem_template(problem_file, base_dir)
    else:
        problems = get_problem_files(base_dir, complexity)
        if not problems:
            print("No problems found")
            return

        problem_file = choice(problems)

    create_problem_template(problem_file, base_dir)


if __name__ == "__main__":
    main()
