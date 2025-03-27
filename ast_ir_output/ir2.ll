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
  %"x" = alloca i32
  store i32 42, i32* %"x"
  %".3" = load i32, i32* %"x"
  %".4" = bitcast [4 x i8]* @".str.3030070452323609682" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 %".3")
  ret void
}
