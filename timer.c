/* timer.c
 *
 * Copyright (c) 2020 Savinelli Roberto Nicolás <rsavinelli@est.frba.utn.edu.ar>
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
#include <stdlib.h>
#include <unistd.h>

#define NOTIFICATION "notify-send \"Time is up!\" \"Timer countdown finished\""
#define BELL "paplay /usr/share/sounds/freedesktop/stereo/complete.oga"

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
    float time;

    if (argc == 1) {
        printf("Usage: ./timer n_minutes\n");
    }

    else {
        if ((time = atof((const char *) argv[1])*60) <= 0 ) {
            printf("timer: invalid input\n");
        }

        else {
            printf("Timer configuration: %.2f m\n\n", time/60);

            while (time > 0) {
                if((int) time % 15 == 0) {
                    printf("%.2d:%.2d\n", (int) time/60, (int) time % 60);
                }
                sleep(1);
                time--;
            }

            printf("Time is up!\n");

            runcommand(NOTIFICATION);
            runcommand(BELL);
        }
    }

    return 0;
}
