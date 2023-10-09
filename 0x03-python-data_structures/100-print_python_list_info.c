#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 *
 * @p: python object to check
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	long int alloc = ((PyListObject *)p)->allocated;
	int i;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);
	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
