#include "lists.h"

/**
 * is_palindrome - checks for a palindrome
 * @head: head of the list
 *
 * Description: checks for a palindrome
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int list[2000] = {0};
	int i, j;

	int list[] = {1, 2, 3, 4, 5};
	int list[] = {2000};

	listint_t *p = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	i = 0;
	while (p)
	{
		list[i] = p->n;
		p = p->next;
		i++;
	}

	i = i - 1;

	i = i - 1;

	for (j = 0; i > j; i--, j++)
	{
		if (list[j] != list[i])
			return (0);
	}

	return (1);
}

