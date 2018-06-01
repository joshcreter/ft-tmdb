from functools import reduce
import operator
from more_itertools import unique_everseen


class MapperUtil:
    @staticmethod
    def map_list(source_list, mapping_dict):
        output = []

        for item in source_list:
            mapped_item = mapping_dict.get(item, item)

            # If the item is not mapped, wrap it in a list
            # Doing this prevents the unmapped item string from exploding into single characters in the next step
            if isinstance(mapped_item, list):
                output.append(mapped_item)
            else:
                output.append([mapped_item])

        if output:
            # Now flatten the list of lists into a simple list
            output = reduce(operator.add, output)

            # Next deduplicate the flattened list
            output = list(unique_everseen(output))

            # Filter out blank items
            output = list(filter(None, output))

        return output