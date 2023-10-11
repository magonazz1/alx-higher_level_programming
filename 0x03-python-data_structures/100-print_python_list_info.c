#include <Python.h>

/**
 * print_python_list_info - function that prints basic info about Python lists
 * @p: Python object list
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
    int size, allocate, b;
    PyObject *objct;

    size = Py_SIZE(p);
    allocate = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", allocate);

    for (b = 0; b < size; b++)
    {
        printf("Element %d: ", b);

        objct = PyList_GetItem(p, b);
        printf("%s\n", Py_TYPE(objct)->tp_name);
    }
}
