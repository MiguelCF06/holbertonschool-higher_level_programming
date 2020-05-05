#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include <Python.h>
/**
 *print_python_list_info - Prints some basic info about python lists
 *@p: The python object (PyObject)
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t lenList = 0;
	const char *elem;
	int x = 0;

	list = (PyListObject *)p;
	lenList = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", lenList);
	printf("[*] Allocated = %ld\n", list->allocated);
	while (x < lenList)
	{
		elem = Py_TYPE(list->ob_item[x])->tp_name;
		printf("Element %d: %s\n", x, elem);
		x++;
	}
}
