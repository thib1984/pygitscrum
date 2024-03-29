"""
--check scripts
"""
from pygitscrum.git import git_code, git_output
from pygitscrum.args import compute_args
from pygitscrum.scan import absolute_path_without_git
from pygitscrum.print import (
    print_resume_list,
    print_debug,
    print_y,
    print_g,
)


def git_check(files):
    """
    entry point for --check
    """
    files_to_work = []
    print_g("Job --check started")
    print_g("git repos found : " + str(len(files)))
    print_g("running...")
    for repo in files:
        repo = absolute_path_without_git(repo)
        print_debug(repo + " ... ")

        while "Your branch is up to date" not in git_output(
            repo, ["status"]
        ):
            if compute_args().fast:
                files_to_work.append(repo)
                break
            print_g(repo)
            print_y(git_output(repo, ["status"]))
            answer = input("p(ull)/P(ush)/s(how)/S(how all)/q(uit)? ")
            hfh = "HEAD..FETCH_HEAD"
            fhh = "FETCH_HEAD..HEAD"
            no = "--name-only"
            if answer == "p":
                git_code(repo, ["pull"])
            elif answer == "P":
                git_code(repo, ["push"])
            elif answer == "S":
                if compute_args().nocolor:
                    git_code(repo, ["log", "-no-color", "-p", hfh])
                    git_code(repo, ["log", "-no-color", "-p", fhh])
                else:
                    git_code(repo, ["log", "-p", hfh])
                    git_code(repo, ["log", "-p", fhh])                        
            elif answer == "s":
                if compute_args().nocolor:
                    git_code(repo, ["log", "-no-color", "-p", no, hfh])
                    git_code(repo, ["log", "-no-color", "-p", no, fhh])
                else: 
                    git_code(repo, ["log", "-p", no, hfh])
                    git_code(repo, ["log", "-p", no, fhh])                       
            else:
                files_to_work.append(repo)
                break

    ############################################
    print_resume_list(files_to_work, "Repos with pull/push available")
    print("")
    if len(files_to_work) == 0:
        print_g("ALL IS OK, GOOD JOB!")
        print("")
    print_g("Job finished")
