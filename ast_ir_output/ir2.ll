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
  %".2" = sitofp i32 2 to float
  %".3" = fmul float 0x400c000000000000, %".2"
  %".4" = sitofp i32 10 to float
  %".5" = fadd float %".4", %".3"
  %"a" = alloca float
  store float %".5", float* %"a"
  %".7" = load float, float* %"a"
  %".8" = bitcast [3 x i8]* @".str.1444584550978747635" to i8*
  %".9" = fpext float %".7" to double
  %".10" = call i32 (i8*, ...) @"printf"(i8* %".8", double %".9")
  ret void
}
