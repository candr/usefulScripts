#include <termios.h>
#include <fcntl.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

int main(int argc, char** argv){
	int dev, r, w, i;
	char awake;
	time_t seconds;
	char* resp;

	dev = open("/dev/ttyUSB0", O_RDWR | O_NOCTTY | O_NDELAY);

	if(dev < 0){
		printf("Could not open, err %i\n", errno);
		return 1;
	}

	struct termios myTermios;
	tcgetattr(dev, &myTermios);
	tcflush(dev, TCIFLUSH);
	myTermios.c_cflag = B9600 | CS8 | CREAD | CLOCAL | HUPCL;
	cfsetospeed(&myTermios, B9600);
	if(tcsetattr(dev, TCSANOW, &myTermios)){
		printf("Could not configure");
		return 1;
	}
	resp = (char*)malloc(512 * sizeof(char));
	seconds = time(NULL);
	while(1){
		if(seconds == time(NULL)) {
			continue;
		} else {
			seconds = time(NULL);
		}
		w = write(dev, "1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,4.0,4.0,4.0", 48);
		if(w < 0){
			printf("Could not write, err %i\n", errno);
			return 1;
		}

		sleep(1);


	}

	return 0;
	free(resp);
}


	
