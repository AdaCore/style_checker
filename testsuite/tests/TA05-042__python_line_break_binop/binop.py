MASK_OPTION_1 = frozenset(['1'])
MASK_OPTION_2 = frozenset(['2'])
MASK_OPTION_3 = frozenset(['3'])
MASK_OPTION_4 = frozenset(['4'])

# In the following statement, we introduce the line breaks after
# the binary operator. We expect the style_checker to accept that.
MASK_ALL = (MASK_OPTION_1 |
            MASK_OPTION_2 |
            MASK_OPTION_3 |
            MASK_OPTION_4)

# In the following statement, we introduce the line breaks before
# the binary operator. We also expect the style_checker to accept that.
MASK_MINUS_3 = (MASK_OPTION_1
                | MASK_OPTION_2
                | MASK_OPTION_4)
