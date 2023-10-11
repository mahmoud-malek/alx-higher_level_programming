#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints info about lists
 * @p: object to print about
 */

void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - prints information about bytes
 * @p: python object to print from
 */

void print_python_bytes(PyObject *p)
{
	char *s;
	Py_ssize_t size, i;

	printf("[*] Python bytes\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	s = PyBytes_AsString(p);

	printf("  Size of the Python Bytes = %ld\n", size);
	printf("  Trying string: %s\n", s);

	if (size < 10)
		printf("  First %ld bytes: ", size + 1);
	else
		printf("  First 10 bytes: ");

	for (i = 0; i < size && i < 10; i++)
		printf("%02hhx ", s[i]);

	printf("\n");
}
