#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints info about lists
 * @py_obj: object to print about
 */

void print_python_list(PyObject *py_obj)
{
	long int list_size, index;
	PyObject *list_item;

	printf("[*] Python list info\n");

	if (!PyList_Check(py_obj))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list_size = ((PyVarObject *)py_obj)->ob_size;
	printf("[*] Size of the Python List = %ld\n", list_size);

	for (index = 0; index < list_size; index++)
	{
		list_item = ((PyListObject *)py_obj)->ob_item[index];
		printf("Element %ld: %s\n", index, list_item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - prints information about bytes
 * @py_obj: python object to print from
 */

void print_python_bytes(PyObject *py_obj)
{
	char *byte_string;
	Py_ssize_t byte_size, index;

	printf("[*] Python bytes\n");

	if (!PyBytes_Check(py_obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byte_size = ((PyVarObject *)py_obj)->ob_size;
	byte_string = ((PyBytesObject *)py_obj)->ob_sval;

	printf("  Size of the Python Bytes = %ld\n", byte_size);
	printf("  Trying string: %s\n", byte_string);

	if (byte_size < 10)
		printf("  First %ld bytes: ", byte_size + 1);
	else
		printf("  First 10 bytes: ");

	for (index = 0; index < byte_size && index < 10; index++)
		printf("%02hhx ", byte_string[index]);

	printf("\n");
}
