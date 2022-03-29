#include <gps.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <errno.h>

int main() {
int rc;
//struct timeval tv;
struct gps_data_t gps_data;

if ((gps_open(GPSD_SHARED_MEMORY, NULL, &gps_data)) == -1) {
    printf("code: %d, reason: %s\n", errno, gps_errstr(errno));
    return EXIT_FAILURE;
}

for(int i=0; i<1; i++) {
        /* read data */
        if ((gps_read(&gps_data)) == -1) {
            printf("error occured reading gps data. code: %d, reason: %s\n", errno, gps_errstr(errno));
        } else {
            /* Display data from the GPS receiver. */
            if ((gps_data.status == STATUS_FIX) && 
                (gps_data.fix.mode == MODE_2D || gps_data.fix.mode == MODE_3D) &&
                !isnan(gps_data.fix.latitude) && 
                !isnan(gps_data.fix.longitude)) {
                    printf("%i,%i", gps_data.fix.latitude, gps_data.fix.longitude);
            } else {
                printf("no GPS data available");
            }
        }

    sleep(3);
}

/* When you are done... */
gps_close (&gps_data);

return EXIT_SUCCESS;
}
