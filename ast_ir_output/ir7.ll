; ModuleID = "my_lang"
target triple = "x86_64-pc-linux-gnu"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"

declare i32 @"printf"(i8* %".1", ...)

declare i32 @"scanf"(i8* %".1", ...)

@".str.3948252993100881646" = internal constant [3 x i8] c"%d\00"
@".str.1444584550978747635" = internal constant [3 x i8] c"%f\00"
define void @"main"()
{
entry:
  %".2" = add i32 2, 3
  %".3" = sub i32 4, 1
  %".4" = mul i32 %".2", %".3"
  %".5" = sdiv i32 10, 2
  %".6" = add i32 %".4", %".5"
  %"x" = alloca i32
  store i32 %".6", i32* %"x"
  %".8" = load i32, i32* %"x"
  %".9" = bitcast [3 x i8]* @".str.3948252993100881646" to i8*
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".9", i32 %".8")
  ret void
}
