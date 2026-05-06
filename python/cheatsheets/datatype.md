# Python Data Types – Quick Memory Guide

| Operation / Function | List | Tuple | Dictionary | Set | String |
|---|---|---|---|---|---|
| Create | `[]` | `()` | `{}` | `{}` / `set()` | `"text"` |
| Example | `[1,2,3]` | `(1,2,3)` | `{"a":"alpha"}` | `{1,2,3}` | `"abc"` |
| Ordered | ✅ | ✅ | ✅ (Python 3.7+) | ❌ | ✅ |
| Mutable | ✅ | ❌ | ✅ | ✅ | ❌ |
| Unique elements | ❌ | ❌ | Keys unique | ✅ | ❌ |

---

# Access / Retrieval

| Operation | List | Tuple | Dictionary | Set | String |
|---|---|---|---|---|---|
| Indexing | `list[i]` | `tup[i]` | `dict[key]` | ❌ | `str[i]` |
| Slicing | `list[a:b]` | `tup[a:b]` | ❌ | ❌ | `str[a:b]` |
| Membership | `x in list` | `x in tup` | `key in dict` | `x in set` | `x in str` |

---

# Add Elements

| Function | List | Tuple | Dictionary | Set | String |
|---|---|---|---|---|---|
| append | `list.append(x)` | ❌ | ❌ | ❌ | ❌ |
| insert | `list.insert(i,x)` | ❌ | ❌ | ❌ | ❌ |
| extend | `list.extend(iter)` | ❌ | ❌ | ❌ | ❌ |
| add | ❌ | ❌ | ❌ | `set.add(x)` | ❌ |
| update | ❌ | ❌ | `dict.update()` | `set.update()` | ❌ |
| new key assignment | ❌ | ❌ | `dict[key]=value` | ❌ | ❌ |

---

# Delete Elements

| Function | List | Tuple | Dictionary | Set | String |
|---|---|---|---|---|---|
| pop() | `list.pop()` | ❌ | `dict.pop(key)` | `set.pop()` | ❌ |
| pop(index) | `list.pop(i)` | ❌ | ❌ | ❌ | ❌ |
| remove(value) | `list.remove(x)` | ❌ | ❌ | `set.remove(x)` | ❌ |
| discard | ❌ | ❌ | ❌ | `set.discard(x)` | ❌ |
| del | `del list[i]` | ❌ | `del dict[key]` | ❌ | ❌ |
| popitem | ❌ | ❌ | `dict.popitem()` | ❌ | ❌ |
| clear | `list.clear()` | ❌ | `dict.clear()` | `set.clear()` | ❌ |

---

# Search / Count

| Function | List | Tuple | Dictionary | Set | String |
|---|---|---|---|---|---|
| count | `list.count(x)` | `tup.count(x)` | ❌ | ❌ | `str.count(x)` |
| index | `list.index(x)` | `tup.index(x)` | ❌ | ❌ | `str.index(x)` |

---

# Built-in Functions

| Function | Works On |
|---|---|
| `len()` | list, tuple, dict, set, string |
| `sum()` | list, tuple |
| `max()` | list, tuple, set, string |
| `min()` | list, tuple, set, string |
| `sorted()` | list, tuple, set, string |
| `reversed()` | list, tuple, string |
| `any()` | iterable |
| `all()` | iterable |
| `enumerate()` | iterable |

---

# Sorting / Ordering

| Function | List | Tuple | Dictionary | Set | String |
|---|---|---|---|---|---|
| sort | `list.sort()` | ❌ | ❌ | ❌ | ❌ |
| sorted | `sorted(list)` | `sorted(tup)` | `sorted(dict)` | `sorted(set)` | `sorted(str)` |
| reverse | `list.reverse()` | ❌ | ❌ | ❌ | ❌ |
| reversed | `reversed(list)` | `reversed(tup)` | ❌ | ❌ | `reversed(str)` |

---

# Dictionary Specific

| Function | Description |
|---|---|
| `dict.keys()` | returns all keys |
| `dict.values()` | returns all values |
| `dict.items()` | returns key-value pairs |

---

# Set Operations

| Function | Description |
|---|---|
| `set.union()` | combine sets |
| `set.intersection()` | common elements |
| `set.difference()` | elements in first set only |

---

# String Functions

| Function | Description |
|---|---|
| `str.upper()` | convert to uppercase |
| `str.lower()` | convert to lowercase |
| `str.split()` | split into list |
| `str.strip()` | remove whitespace |
| `str.replace()` | replace substring |
| `str.count()` | count occurrences |
| `str.index()` | find index |

---

# One-Line Memory Trick

| Data Type | Key Idea |
|---|---|
| List | Ordered + Mutable |
| Tuple | Ordered + Immutable |
| Dict | Key-Value Mapping |
| Set | Unique Unordered Elements |
| String | Immutable Text Sequence |

---

# Python Data Types – Operations Quick Reference

| Operation / Function | List | Tuple | Dictionary | Set | String |
|---|---|---|---|---|---|
| Create | `[]`, `[1,2]` | `()`, `(1,2)` | `{}`, `{"a":"alpha"}` | `{1,2}`, `set()` | `"abc"` |
| Access element | `list[i]` | `tup[i]` | `dict[key]` | ❌ | `str[i]` |
| Slicing | `list[a:b]` | `tup[a:b]` | ❌ | ❌ | `str[a:b]` |
| Membership check | `x in list` | `x in tup` | `key in dict` | `x in set` | `x in str` |
| Update existing | `list[i] = v` | ❌ | `dict[key] = v` | ❌ | ❌ |
| Add element | `append(x)` | ❌ | `dict[key]=v` | `add(x)` | ❌ |
| Insert at position | `insert(i,x)` | ❌ | ❌ | ❌ | ❌ |
| Extend multiple | `extend(iter)` | ❌ | `update()` | `update(iter)` | ❌ |
| Remove last | `pop()` | ❌ | ❌ | `pop()` | ❌ |
| Remove by index | `pop(i)` | ❌ | ❌ | ❌ | ❌ |
| Remove by value | `remove(x)` | ❌ | `pop(key)` | `remove(x)` | ❌ |
| Safe remove | ❌ | ❌ | ❌ | `discard(x)` | ❌ |
| Delete element | `del list[i]` | ❌ | `del dict[key]` | ❌ | ❌ |
| Remove last pair | ❌ | ❌ | `popitem()` | ❌ | ❌ |
| Clear all | `clear()` | ❌ | `clear()` | `clear()` | ❌ |
| Count occurrences | `count(x)` | `count(x)` | ❌ | ❌ | `count(x)` |
| Find index | `index(x)` | `index(x)` | ❌ | ❌ | `index(x)` |
| Length | `len()` | `len()` | `len()` | `len()` | `len()` |
| Sum elements | `sum()` | `sum()` | ❌ | ❌ | ❌ |
| Maximum | `max()` | `max()` | `max(keys)` | `max()` | `max()` |
| Minimum | `min()` | `min()` | `min(keys)` | `min()` | `min()` |
| Sort in place | `sort()` | ❌ | ❌ | ❌ | ❌ |
| Return sorted | `sorted()` | `sorted()` | `sorted(keys)` | `sorted()` | `sorted()` |
| Reverse in place | `reverse()` | ❌ | ❌ | ❌ | ❌ |
| Reverse iterator | `reversed()` | `reversed()` | ❌ | ❌ | `reversed()` |
| Iterate with index | `enumerate()` | `enumerate()` | `enumerate(keys)` | `enumerate()` | `enumerate()` |
| Any true element | `any()` | `any()` | `any(keys)` | `any()` | `any()` |
| All true elements | `all()` | `all()` | `all(keys)` | `all()` | `all()` |
| Get keys | ❌ | ❌ | `keys()` | ❌ | ❌ |
| Get values | ❌ | ❌ | `values()` | ❌ | ❌ |
| Get items | ❌ | ❌ | `items()` | ❌ | ❌ |
| Set union | ❌ | ❌ | ❌ | `union()` | ❌ |
| Set intersection | ❌ | ❌ | ❌ | `intersection()` | ❌ |
| Set difference | ❌ | ❌ | ❌ | `difference()` | ❌ |
| Uppercase | ❌ | ❌ | ❌ | ❌ | `upper()` |
| Lowercase | ❌ | ❌ | ❌ | ❌ | `lower()` |
| Split string | ❌ | ❌ | ❌ | ❌ | `split()` |
| Strip spaces | ❌ | ❌ | ❌ | ❌ | `strip()` |
| Replace substring | ❌ | ❌ | ❌ | ❌ | `replace()` |
