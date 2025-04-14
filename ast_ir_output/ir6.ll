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
  %".2" = fpext float 0x4016000000000000 to double
  %"a" = alloca double
  store double %".2", double* %"a"
  %".4" = load double, double* %"a"
  %".5" = bitcast [3 x i8]* @".str.1444584550978747635" to i8*
  %".6" = call i32 (i8*, ...) @"printf"(i8* %".5", double %".4")
  ret void
}
