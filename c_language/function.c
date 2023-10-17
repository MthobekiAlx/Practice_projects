#include "main.h"
#include <stdio.h>
#include <stdarg.h>
/**
 * print_char - prints character
 * @args: character argument
 * Return: number of characters
 */
int print_char(va_list args)
{
	int c;

	c = va_arg(args, int);
	return (__putchar(c));
}
/**
 * print_string - prints a string
 * @args: string  argument
 * Return: number of characters
 */
int print_string(va_list args)
{
	int i, count = 0;
	char *str;

	i = 0;
	str = va_arg(args, char*);
	if (str == NULL)
		str = "(null)";
	while (str[i] != '\0')
	{
		__putchar(str[i]);
		i++;
		count++;
	}
	return (count);
}
/**
 * print_percent - pass the percent sing
 * @args: string  argument
 * Return: return the percent sing
 *
 */
int print_percent(va_list args)
{
	char *str;

	str = "%";
	if (va_arg(args, int) == *str)
	{
		return (*str);
	}
	return (*str);
}

/**
 * print_dec - prints a decimal
 * @args: decimal argument
 * Return: counter
 */
int print_dec(va_list args)
{

	unsigned int absolute, aux, countnum, count;
	int n;

	count = 0;
	n = va_arg(args, int);
		if (n < 0)
		{
			absolute = (n * -1);
			count += __putchar('-');
		}
		else
			absolute = n;

	aux = absolute;
	countnum = 1;
	while (aux > 9)
	{
		aux /= 10;
		countnum *= 10;
	}
	while (countnum >= 1)
	{
		count += __putchar(((absolute / countnum) % 10) + '0');
		countnum /= 10;
	}
	return (count);
}
/**
 * print_int - prints integer
 * @args: integer argument
 * Return: the decimal function
 */

int print_int(va_list args)
{
	return (print_dec(args));
}
