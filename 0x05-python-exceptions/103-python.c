#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Prints information about a PyFloatObject
 * @p: The PyObject
 *
 * Description: This function prints the value of a PyFloatObject.
 * If the object is not a valid PyFloatObject, it prints an error message.
 */

void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}

/**
 * print_python_bytes - Prints information about a PyBytesObject
 * @p: The PyObject
 *
 * Description: This function prints the size, string value, and the first
 * 10 bytes of a PyBytesObject. If the object is not a valid PyBytesObject,
 * it prints an error message.
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = ((PyBytesObject *)(p))->ob_sval;
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}

	printf("\n");
}

/**
 * print_python_list - Prints information about a PyListObject
 * @p: The PyObject
 *
 * Description: This function prints the size, allocated memory, and the
 * elements of a PyListObject. If the object is not a valid PyListObject,
 * it prints an error message. If an element is a PyBytesObject or
 *  a PyFloatObject,
 * it calls the respective functions to print their information.
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (!PyList_CheckExact(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	while (i < size)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);

		else if (PyFloat_Check(item))
			print_python_float(item);

		i++;
	}
}
