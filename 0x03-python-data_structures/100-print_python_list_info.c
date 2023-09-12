#include <Python.h>

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A PyObject list.
*/
void print_python_list_info(PyObject *p)
{
	int size_p, alloc_p, i;
	PyObject *obj;

	size_p = Py_SIZE(p);
	alloc_p = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size_p);
	printf("[*] Allocated = %d\n", alloc_p);

	for (i = 0; i < size_p; i++)
	{
		printf("Element %d:", i);

		obj = PyList_Getitem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
