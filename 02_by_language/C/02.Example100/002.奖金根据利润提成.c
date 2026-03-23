#include <stdio.h>

int main() {

    double i;
    double a = i * 0.1;
    double b = (i - 100000) * 0.075 + 10000;
    double c = (i - 200000) * 0.05 + 17500;
    double d = (i - 400000) * 0.03 + 27500;
    double e = (i - 600000) * 0.015 + 33500;
    double f = (i - 1000000) * 0.01 + 39500;

    scanf("%lf", &i);

    printf("奖金分成是");

    if (i <= 100000){
        printf("%f",a);
    }
    else if (i <= 200000){
        printf("%f",b);
    }
    else if (i <= 400000){
        printf("%f",c);
    }
    else if (i <= 600000){
        printf("%f",d);
    }
    else if (i <= 1000000){
        printf("%f",e);
    }
    else if (i >= 1000000){
        printf("%f",f);
    }
    return 0;
}
