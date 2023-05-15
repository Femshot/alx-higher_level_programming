#include <Python.h>
#include <stdio.h>

/**
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = 0;

	if (!(PyList_check(p)))
		return 0;

	list_size = PyList_Size(p);

	printf("[*] Size of the Python List = %d", (int)list_size);
}
