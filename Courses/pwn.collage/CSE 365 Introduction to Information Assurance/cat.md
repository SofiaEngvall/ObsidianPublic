int main(int argc, char **argv) {
	char buf[1024];
	int n;
	int fd = argc == 1 ? 0 : open(argv[1], 0);
	puts("Hi dude!");
	while ((n = read(fd, buf, 1024)) > && write(1, buf, n) > 0);
}

gcc -o cat cat.c