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
  %".2" = sdiv i32 7, 2
  %"b" = alloca i32
  store i32 %".2", i32* %"b"
  %".4" = sitofp i32 2 to float
  %".5" = fdiv float 0x401c000000000000, %".4"
  %"c" = alloca float
  store float %".5", float* %"c"
  %".7" = load i32, i32* %"b"
  %".8" = bitcast [3 x i8]* @".str.3948252993100881646" to i8*
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".8", i32 %".7")
  %".10" = load float, float* %"c"
  %".11" = bitcast [3 x i8]* @".str.1444584550978747635" to i8*
  %".12" = fpext float %".10" to double
  %".13" = call i32 (i8*, ...) @"printf"(i8* %".11", double %".12")
  ret void
}
