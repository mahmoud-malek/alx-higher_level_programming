#include <Python.h>

/**
 * print_python_list - prints info about lists
 * @p: object to print about
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < size; i++)
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}

/**
 * print_python_bytes - prints information about bytes
 * @p: python object to print from
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	long int size;
	int i;

	printf("[*] Python bytes\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	str = PyBytes_AS_STRING(p);
	size = PyBytes_Size(p);
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %ld bytes: ", size + 1);
	else
		printf("  first 10 bytes: ");
	for (i = 0; i < size && i < 9; i++)
		printf("%02hhx ", str[i]);
	printf("%02hhx\n", str[i]);
}
