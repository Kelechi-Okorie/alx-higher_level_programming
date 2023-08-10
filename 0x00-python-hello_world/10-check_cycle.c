#include "lists.h"

/**
 * check_cycle - checks for cycle in a linked list
 * @list: head of the linked list
 *
 * Description: checks for cycle in a lined list
 * Return: 0 if there no cycle
 * 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *p;
	listint_t *q;

	p = list;
	q = list;

	while (p && q && q->next)
	{
		p = p->next;
		q = q->next->next;

		if (p == q)
			return (1);
	}

	return (0);
}
