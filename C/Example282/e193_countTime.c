#include <stdio.h>

struct time
{
    int hour;
    int minute;
    int second;
}t;

int main()
{
    FILE *fp;
    fp=fopen("Time", "r");
    fread(&t, sizeof(struct time), 1, fp);
    while(!kbhit())
    {
        rewind(fp);
        sleep(1);
        fread(&t, sizeof(struct time), 1, fp);
        if(t.second==59)
        {
            t.minute=t.minute+1;
            if(t.second==60)
            {
                t.hour=t.hour+1;
                t.minute=0;
            }
            t.second=0;
        }
        else
            t.second=t.second+1;
        print("%d:%d:%d\n", t.hour,t.minute,t.second);
        fp=fopen("Time", "w");
        fwrite(&t, sizeof(struct time), 1, fp);
        fclose(fp);
    }
}