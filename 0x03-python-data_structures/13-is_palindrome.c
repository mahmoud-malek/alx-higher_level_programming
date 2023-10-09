#include "lists.h"
#include <stdlib.h>

/**
 * is_palindrome - checks if the list is a palindrome
 * @head: is the head node of the linked list
 * Return: 1 if palindrome and 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	int len = 0, i = 0, j = 0;
	listint_t *temp = *head;
	int *store = NULL;

	if (!head || !*head)
		return (1);

	while (temp)
	{
		temp = temp->next;
		len++;
	}

	store = malloc(len * sizeof(int));
	if (!store)
		return (-1);

	temp = *head;
	while (temp)
	{
		store[j++] = temp->n;
		temp = temp->next;
	}

	for (j -= 1; i < j; i++, j--)
		if (i < j && store[i] != store[j])
		{
			free(store);
			return (0);
		}

	free(store);
	return (1);
}
