#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: Linked list to check
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;

	slow = fast = list;
	while (list != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
