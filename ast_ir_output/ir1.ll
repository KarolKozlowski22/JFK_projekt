; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.3030070452323609682" = internal constant [4 x i8] c"%d\0a\00"
@".str.6390100985560808981" = internal constant [4 x i8] c"%f\0a\00"
define void @"main"()
{
entry:
  %".2" = bitcast [4 x i8]* @".str.6390100985560808981" to i8*
  %".3" = fpext float 0x4039666660000000 to double
  %".4" = call i32 (i8*, ...) @"printf"(i8* %".2", double %".3")
  ret void
}
