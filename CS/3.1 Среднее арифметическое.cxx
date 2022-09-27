#include <stdio.h> // Подключение к библиотеке ввода - вывода
int main() // Начало главной функции
{
    printf("Введите первое число ");
    float fr;
    scanf("%f", &fr);
    printf("Введите второе число ");
    float sc;
    scanf("%f", &sc);
    float avr;
    avr = (fr + sc) / 2;
    printf("%f", avr);
    return 0;
}