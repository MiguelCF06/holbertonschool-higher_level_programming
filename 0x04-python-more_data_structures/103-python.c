#include <Python.h>
#include <stdio.h>
#include "Python.h"
/**
 *print_python_bytes - Print info about bytes of a python list
 *@p: Python object list
 */
void print_python_bytes(PyObject *p)
{
	int x;

	if (PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  size: %lu\n", PyBytes_Size(p));
		printf("  trying string: %s\n", PyBytes_AsString(p));
		if (PyBytes_Size(p) >= 10)
			printf("  first 10 bytes: ");
		else
			printf("  first %lu bytes: ", PyBytes_Size(p) + 1);
		for (x = 0; x < PyBytes_Size(p) && x <= 9; x++)
		{
			printf("%02hhx", (PyBytes_AsString(p)[x]));
			if (x < 9)
				printf(" ");
		}
		if (PyBytes_Size(p) < 10)
			printf("00\n");
		else
			printf("\n");
	}
	else
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}
/**
 *print_python_list - Print some basic info about python list
 *@p: The python object list
 */
void print_python_list(PyObject *p)
{
	long int x;
	PyObject *items;
	Py_ssize_t lenList = 0;

	lenList = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %lu\n", PyList_Size(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)(p))->allocated);
	for (x = 0; x < lenList; x++)
	{
		items = PyList_GET_ITEM(p, x);
		printf("Element %lu: ", x);
		printf("%s\n", (((PyObject *)(items))->ob_type)->tp_name);
		if (PyBytes_Check(items))
			print_python_bytes(items);
	}
}
