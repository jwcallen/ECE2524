#include <cstdlib>
#include <iostream>

#include <signal.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void) {
	int pipefd[2];
	pid_t generator, consumer;
	int status;

	if (pipe(pipefd) < 0) {
		std::cerr << "pipe(2) failed, aborting!" << std::endl;
		std::abort();
	}

	if (!(generator = fork())) {
		close(pipefd[0]);
		dup2(pipefd[1], 1);
		execl("./generator", "./generator", (char *) NULL);
	}

	if (!(consumer = fork())) {
		close(pipefd[1]);
		dup2(pipefd[0], 0);
		execl("./consumer", "./consumer", (char *) NULL);
	}
	// note: must close both ends of the pipe here, or else children may not complete normally
	close(pipefd[0]);
	close(pipefd[1]);

	sleep(1);

	kill(generator, SIGTERM);

	waitpid(generator, &status, 0);
	if (WIFEXITED(status))
		std::cerr << "child[" << generator << "] exited with status " << WEXITSTATUS(status) << std::endl;
	else if (WIFSIGNALED(status))
		std::cerr << "child[" << generator << "] exited with signal " << WTERMSIG(status) << std::endl;
	else
		std::cerr << "child[" << generator << "] exited neither normally nor via signal?" << std::endl;

	waitpid(consumer, &status, 0);
	if (WIFEXITED(status))
		std::cerr << "child[" << consumer << "] exited with status " << WEXITSTATUS(status) << std::endl;
	else if (WIFSIGNALED(status))
		std::cerr << "child[" << consumer << "] exited with signal " << WTERMSIG(status) << std::endl;
	else
		std::cerr << "child[" << consumer << "] exited neither normally nor via signal?" << std::endl;

	return 0;
}
