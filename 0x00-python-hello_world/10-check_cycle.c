#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: Linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *head = NULL;

	if (list)
		head = list;
	while (list != NULL)
	{
		list = list->next;
		if (list && head == list)
			return (1);
	}
	return (0);
}
