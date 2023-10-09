#include "lists.h"

/**
 * is_palindrome - checks if the list is a palindrome
 * @head: is the head node of the linked list
 * Return: 1 if palindrome and 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j = 0;
	listint_t *temp = *head;
	listint_t *current = *head;

	if (!head || !*head)
		return (1);

	while (temp != NULL)
	{
		temp = temp->next;
		len++;
	}

	temp = *head;
	for (; current && i < (len / 2); i++, current = current->next)
	{
		j = i;
		temp = current;
		while (temp && j < (len - i - 1))
			temp = temp->next, j++;

		if (temp && temp->n != current->n)
			return (0);
	}

	return (1);
}
