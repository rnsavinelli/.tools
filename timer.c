/* timer.c
 *
 * Copyright (c) 2020 Savinelli Roberto Nicolás <rsavinelli@frba.utn.edu.ar>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
*/

#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include <unistd.h>

#define SECONDS 1
#define MINUTES 60
#define HOURS   3600

#define NOTIFICATION "notify-send \"Time is up!\" \"Timer countdown finished\""
#define BELL "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"

#define ERROR -1

#define printhelp() printf("Usage: ./timer [-s|-m|-h] time\n\nTime format options:\n\t-s: seconds\n\t-n: minutes\n\t-h: hours\n\nExample: ./timer -h 2 -m 45 -s 30\n")

void
runcommand(const char *cmd)
{
	FILE *fp;

	if (!(fp = popen(cmd, "r"))) {
		perror("popen");
		return;
	}

	if (pclose(fp) < 0) {
		perror("pclose");
		return;
	}
}

int
main (int argc, char *argv[])
{
    int time = 0;
    int hours, minutes, seconds;
    int base;

    if (argc <= 2) {
        printhelp();
        return 0;
    }

    else {
        for(int i = 1; i < argc; i++) {
            char* opt = argv[i];

            if(strcmp(opt, "-s") == 0) {
                base = SECONDS;
            }

            else if(strcmp(opt, "-m") == 0) {
                base = MINUTES;
            }

            else if(strcmp(opt, "-h") == 0) {
                base = HOURS;
            }

            else {
                printhelp();
                return ERROR;
            }

            if((i+1) == argc || !isdigit(*argv[i+1])) {
                printhelp();
                return ERROR;
            }

            time += atoi((const char *) argv[++i]) * base;
        }

        if (time < 0 || time > 24 * HOURS) {
            printf("Warning: Invalid input.\n");
            return ERROR;
        }

        else {
            while (time >= 0) {
                hours = time / 3600;
                minutes = (time % 3600) / 60;
                seconds = (time % 3600) % 60;

                printf("\rTime remaining: %02d:%02d:%02d", hours, minutes, seconds);
                fflush(stdout);
                sleep(1);
                time--;
            }

            printf("\nTime is up!\n");

            runcommand(NOTIFICATION);
            runcommand(BELL);
        }
    }

    return 0;
}
