################################################################################
# Automatically-generated file. Do not edit!
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include USB_DEVICE/Target/subdir.mk
-include USB_DEVICE/App/subdir.mk
-include Middlewares/ST/STM32_USB_Device_Library/Core/Src/subdir.mk
-include Middlewares/ST/STM32_USB_Device_Library/Class/CDC/Src/subdir.mk
-include Drivers/STM32F1xx_HAL_Driver/Src/subdir.mk
-include Core/Startup/subdir.mk
-include Core/Src/subdir.mk
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
TestBench_ISIB_UC.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
TestBench_ISIB_UC.list \


# All Target
all: TestBench_ISIB_UC.elf secondary-outputs

# Tool invocations
TestBench_ISIB_UC.elf: $(OBJS) $(USER_OBJS) D:\geoff\Documents\OneDrive\ -\ he2b.be\Ecole\ 2019\ -\ 2020\Q2\Bureau_Etude\1803\ -\ Banc\ d_essais\ Moteur\BANC_ESSAI_ELECTRONIQUE\Microcontroleur\Stm32CubeMXWorkspace\TestBench_ISIB_UC\STM32F103C8TX_FLASH.ld
	arm-none-eabi-gcc -o "TestBench_ISIB_UC.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m3 -T"D:\geoff\Documents\OneDrive - he2b.be\Ecole 2019 - 2020\Q2\Bureau_Etude\1803 - Banc d_essais Moteur\BANC_ESSAI_ELECTRONIQUE\Microcontroleur\Stm32CubeMXWorkspace\TestBench_ISIB_UC\STM32F103C8TX_FLASH.ld" --specs=nosys.specs -Wl,-Map="TestBench_ISIB_UC.map" -Wl,--gc-sections -static --specs=nano.specs -mfloat-abi=soft -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

TestBench_ISIB_UC.list: $(EXECUTABLES)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "TestBench_ISIB_UC.list"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) *
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST)

.PHONY: all clean dependents
.SECONDARY:

-include ../makefile.targets
