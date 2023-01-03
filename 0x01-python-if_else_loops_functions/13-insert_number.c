#include "lists.h"
listint_t *new_node(listint_t **head, listint_t *ini, listint_t *ne, int num);
/**
 *insert_node - function that inserts a node in a sorted list
 *@head: pointer to the first node of the list
 *@number: int to add in the new node
 *Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ini_node = NULL, *newer_node = NULL;
	listint_t *prev_node = NULL;

	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		newer_node = new_node(head, ini_node, NULL, number);
		*head = newer_node;
		return (newer_node);
	}
	ini_node = *head;
	while (*head != NULL)
	{
		prev_node = *head;
		*head = (*head)->next;
		if (*head != NULL && prev_node->n >= number)
		{
			newer_node = new_node(head, ini_node, prev_node, number);
			ini_node = newer_node;
			break;
		}
		else if (*head != NULL && (*head)->n >= number)
		{
			newer_node = new_node(head, ini_node, *head, number);
			prev_node->next = newer_node;
			break;
		}
		else if (*head == NULL)
		{
			newer_node = new_node(head, ini_node, NULL, number);
			prev_node->next = newer_node;
		}
	}
	*head = ini_node;
	return (newer_node);
}

/**
 *new_node - function that creates a new node
 *@head: struct with all needed data
 *@ini: initial node
 *@ne: next node value
 *@num: number to add to the new node
 *Return: address of the new node
 */
listint_t *new_node(listint_t **head, listint_t *ini, listint_t *ne, int num)
{
	listint_t *new_node = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		*head = ini;
		return (NULL);
	}
	new_node->n = num;
	new_node->next = ne;
	return (new_node);
}
