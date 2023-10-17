#include "main.h"

/**
 * get_function - look for the specifier
 * @x: variable to the function
 * Return: function
 */
int (*get_function(char x))(va_list)
{
	int i = 0;
	spec arr[] = {
		{"c", print_char},
		{"s", print_string},
		{"%", print_percent},
		{"d", print_dec},
		{"i", print_int},
		{NULL, NULL}
	};
	while (arr[i].valid)
	{
		if (x == arr[i].valid[0])
			return (arr[i].f);
		i++;
	}
	return (NULL);
}

