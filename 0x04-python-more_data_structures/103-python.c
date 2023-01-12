#include <Python.h>
#include <stdio.h>
#define PY_REP(x) (((PyObject *)(x))->ob_type)
#define DATATYPE PY_REP(((PyListObject *)(p))->ob_item[i])->tp_name
void print_python_bytes(PyObject *p);
/**
 *print_python_list - function to print about list
 *@p: pointer to refer to a list of python
 *Return: Nothing
 */
void print_python_list(PyObject *p)
{
	int i = 0, tamano = 0;

	tamano = (int)(((PyVarObject *)(p))->ob_size);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", tamano);
	printf("[*] Allocated = %d\n", (int)(((PyListObject *)(p))->allocated));
	for (i = 0; i < tamano; i++)
	{
		printf("Element %d: %s\n", i, DATATYPE);
		if (PyBytes_Check((((PyListObject *)(p))->ob_item[i])))
			print_python_bytes((((PyListObject *)(p))->ob_item[i]));
	}
}
/**
 *print_python_bytes - function to print about list
 *@p: pointer to refer to a byte object of python
 *Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	int tamano = 0, printed = 0, i = 0;
	char *buffer = NULL;
	Py_ssize_t length = NULL;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		PyBytes_AsStringAndSize(p, &buffer, &length);
		tamano = (int)length;
		if (tamano >= 10)
			printed = 10;
		else
			printed = tamano + 1;
		printf("  size: %d\n", tamano);
		printf("  trying string: %s\n", buffer);
		printf("  first %d bytes: ", printed);
		for (i = 0; i < printed; i++)
		{
			printf("%02x", (unsigned char)*(buffer + i));
			if (i < printed - 1)
				printf(" ");
		}
			printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");

}

