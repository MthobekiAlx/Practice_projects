#ifndef MAIN_H
#define MAIN_H

#include <stdio.h>
#include <stdarg.h>

/**
 * struct specifier - struct specifier
 * @valid: the valid character.
 * @p: the functions associated.
 *
 */

typedef struct specifier
{
	char *valid;
	int (*f)(va_list arg);
} spec;

int _printf(const char *format, ...);
int print_char(va_list args);
int print_string(va_list args);
int print_dec(va_list args);
int print_int(va_list args);
int __putchar(char c);
int print_percent(va_list args);
int (*get_function(char x))(va_list args);

#endif /* MAIN_H */
