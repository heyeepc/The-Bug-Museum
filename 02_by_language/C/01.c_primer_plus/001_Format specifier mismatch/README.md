alphabet是一个 char[26]类型的数组（数组名在大多数情况下会退化为指向首元素的指针），而 %c格式符期望一个 char类型的单个字符。

// 错误：传递数组指针给%c
printf("%c", alphabet);  // alphabet 实际上是 char* 类型

// 正确：传递单个字符
printf("%c", alphabet[0]);  // 打印第一个字符 'a'

%c：用于打印单个字符
•
%s：用于打印字符串（以 '\0' 结尾的字符数组）

即使将代码改为：

printf("%s", alphabet);  // 仍然错误

因为数组没有以空字符 '\0' 结尾，使用 %s打印会导致越界访问，这是未定义行为。


// 方案1：使用字符串（自动包含\0）
char alphabet[] = "abcdefghijklmnopqrstuvwxyz";
printf("%s", alphabet);

// 方案2：使用循环逐个打印
for(int i = 0; i < 26; i++) {
    printf("%c", alphabet[i]);
}

// 方案3：确保数组以\0结尾
char alphabet[27] = {'a','b','c',...,'z','\0'};
printf("%s", alphabet);
