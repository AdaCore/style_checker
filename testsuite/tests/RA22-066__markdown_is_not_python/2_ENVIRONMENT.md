Now we'll need to edit the arm/cortexm.py file to add support for generating a run-time for 'mystm32':

```
    diff --git a/arm/cortexm.py b/arm/cortexm.py
    index 307ec13..412b795 100644
    --- a/arm/cortexm.py
    +++ b/arm/cortexm.py
         def cortex(self):
             if self.mcu.startswith('stm32f4'):
                 return 'cortex-m4'
    +        elif self.mcu == 'mystm32':
    +            return 'cortex-m4'
             elif self.mcu.startswith('stm32f7'):
                 return 'cortex-m7'
             else:
                 self.mcu = 'stm32f7x'
             elif self.board == 'stm32f769disco':
                 self.mcu = 'stm32f7x9'
    +        elif self.board == 'mystm32':
    +            self.mcu = 'mystm32'
             else:
                 assert False, "Unknown stm32 board: %s" % self.board
```
