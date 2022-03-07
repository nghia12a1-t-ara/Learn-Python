################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Startup/subdir.mk
-include Src/subdir.mk
-include Generate/Src/subdir.mk
-include subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
Bai1.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
Bai1.list \

OBJCOPY_BIN += \
Bai1.bin \


# All Target
all: Bai1.elf secondary-outputs

# Tool invocations
Bai1.elf: $(OBJS) $(USER_OBJS) D:\Python\Python_Repo\Learn-Python\GUI\Example\Bai1\STM32F401RETX_FLASH.ld
	arm-none-eabi-gcc -o "Bai1.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m4 -T"D:\Python\Python_Repo\Learn-Python\GUI\Example\Bai1\STM32F401RETX_FLASH.ld" --specs=nosys.specs -Wl,-Map="Bai1.map" -Wl,--gc-sections -static -L"D:\IOT302_Funix\SDK_1.0.3_NUCLEO-F401RE\lib_stm" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

Bai1.list: $(EXECUTABLES)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "Bai1.list"
	@echo 'Finished building: $@'
	@echo ' '

Bai1.bin: $(EXECUTABLES)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "Bai1.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
