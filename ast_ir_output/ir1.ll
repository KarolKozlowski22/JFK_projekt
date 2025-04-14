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
  %".2" = fmul float 0x4000000000000000, 0x4008000000000000
  %".3" = fadd float 0x4014000000000000, %".2"
  %".4" = fsub float %".3", 0x3ff0000000000000
  %"y" = alloca float
  store float %".4", float* %"y"
  %".6" = load float, float* %"y"
  %".7" = bitcast [3 x i8]* @".str.1444584550978747635" to i8*
  %".8" = fpext float %".6" to double
  %".9" = call i32 (i8*, ...) @"printf"(i8* %".7", double %".8")
  ret void
}
