#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_bytes - Prints bytes information
 * @p: Python Object
 */

void print_python_bytes(PyObject *p)
{
	long int size, i, maxi;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		maxi = 10;
	else
		maxi = size + 1;

	printf("  first %ld bytes:", maxi);

	for (i = 0; i < maxi; i++)
		if (string[i] >= 0)
			printf(" %02x", string[i]);
		else
			printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list - Prints list information
 * @p: Python Object
 */

void print_python_list(PyObject *p)
{
	long int size, i;
	PyObject *o;
	PyListObject *list;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		o = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((o)->ob_type)->tp_name);
		if (PyBytes_Check(o))
			print_python_bytes(o);
	}
}
