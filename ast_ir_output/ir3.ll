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
  %"first" = alloca i32
  store i32 10, i32* %"first"
  %"second" = alloca i32
  store i32 5, i32* %"second"
  %".4" = load i32, i32* %"first"
  %".5" = load i32, i32* %"second"
  %".6" = load i32, i32* %"first"
  %".7" = mul i32 %".5", %".6"
  %".8" = add i32 %".4", %".7"
  store i32 %".8", i32* %"first"
  %".10" = load i32, i32* %"first"
  %".11" = bitcast [4 x i8]* @".str.3030070452323609682" to i8*
  %".12" = call i32 (i8*, ...) @"printf"(i8* %".11", i32 %".10")
  ret void
}
