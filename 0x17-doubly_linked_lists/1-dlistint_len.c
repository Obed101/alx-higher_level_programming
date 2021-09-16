#include "stddef.h"
#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * print_dlistint - a function that prints the number of elements in a list
 *
 * @h: The list
 * Return: Number of elements in the list
 */
size_t dlistint_len(const dlistint_t *h)
{
  if(h != NULL)
    if (sizeof(h) % 4 == 0)
      return (sizeof(h) / 4);
  return (0);
}
