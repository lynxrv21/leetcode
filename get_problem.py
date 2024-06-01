import sys
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


def main() -> None:
    base_dir = Path(__file__).parent

    # Parse the complexity argument if provided
    complexity = None
    if len(sys.argv) > 1:
        complexity = sys.argv[1].lower()
        print(complexity)
        if complexity not in ("easy", "medium", "hard"):
            print("Invalid complexity level. Choose from: easy, medium, hard.")
            return

    problems = get_problem_files(base_dir, complexity)
    if not problems:
        print("No problems found")
        return

    random_problem = choice(problems)

    create_problem_template(random_problem, base_dir)


if __name__ == "__main__":
    main()
