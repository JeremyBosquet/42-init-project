# Style
_END		:=	\033[0m
_BOLD		:=	\033[1m
_UNDER		:=	\033[4m
_REV		:=	\033[7m

# Colors
_GREY		:=	\033[30m
_RED		:=	\033[31m
_GREEN		:=	\033[32m
_YELLOW		:=	\033[33m
_BLUE		:=	\033[34m
_PURPLE		:=	\033[35m
_CYAN		:=	\033[36m
_WHITE		:=	\033[37m

CC := gcc

CFLAGS := _FLAGS

PROJECT := $$

HEADER_SRCS := includes/$$.h libft/libft.h

SRCS :=		main.c

OBJS := $(addprefix objs/, $(SRCS:.c=.o))

OBJS_DIRS := $(sort $(dir $(OBJS)))

INCLUDE := $(sort $(addprefix -I,$(dir $(HEADER_SRCS))))

NAME := $(PROJECT)

all: libft $(NAME)
	@printf "\033[2K\r$(_GREEN)$(_BOLD)Done.\n"

$(NAME): Makefile libft/libft.a $(OBJS)
	@$(CC) $(CFLAGS) $(INCLUDE) $(OBJS) libft/libft.a -o $@
	@printf "%-30b%b" "\033[2K\r$(_GREEN)  $@" "$(_BOLD)[OK]$(_END)\n\n"

$(OBJS): | $(OBJS_DIRS)

$(OBJS_DIRS):
	@mkdir -p $@
	@printf "%-30b%b" "\033[2K\r$(_GREEN)  $(NAME)" "$(_CYAN)[$@ created]$(_END)\n"

objs/%.o: srcs/%.c libft/libft.a $(HEADER_SRCS)
	@printf "%-30b%b" "\033[2K\r$(_YELLOW)  $(NAME)" "\033[1m[$<]\033[0m"
	@$(CC) $(CFLAGS) $(INCLUDE) -c $< -o $@

libft:
	@printf "$(_CYAN)$(_BOLD)Compilation:$(_END)\n"
	@$(MAKE) -s -C libft

clean:
	@rm -rf $(OBJS)
	@$(MAKE) clean -C libft
	@printf "\033[2K\r$(_RED)$(NAME): All objects files have been deleted. $(_END)\n"

fclean: clean
	@$(RM) $(NAME)
	@$(MAKE) fcleaned -C libft
	@printf "\033[2K\r$(_RED)$(NAME): '"$(NAME)"' has been deleted. $(_END)\n\n"

ffclean:
	@rm -rf $(OBJS_DIRS)
	@$(RM) $(NAME)
	@$(MAKE) ffclean -C libft
	@printf "\033[2K\r$(_RED)$(NAME): objs folder has been deleted. $(_END)\n"
	@printf "\033[2K\r$(_RED)$(NAME): '"$(NAME)"' has been deleted. $(_END)\n"

re: fclean all

norme:
	@norminette srcs includes libft

.PHONY: all libft clean fclean ffclean re norme